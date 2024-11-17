package main.java.com.um.prog;
import main.java.com.um.prog.Entities.*;

import java.util.LinkedList;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.PriorityBlockingQueue;


public class Main {
    public static void main(String[] args) {
        PriorityBlockingQueue<Payment> QueueOfPayments = new PriorityBlockingQueue<Payment>(100,Payment::compareTo);
        PriorityBlockingQueue<Payment> QueueOfProcessedPayments = new PriorityBlockingQueue<Payment>(100,Payment::compareTo);
        PriorityBlockingQueue<Payment> QueueOfPackedPayments = new PriorityBlockingQueue<Payment>(100,Payment::compareTo);
        LinkedList<String> listOfBanks = new LinkedList<>();
        LinkedList<Payment> listOfFinishedPayments = new LinkedList<>();

        listOfBanks.add("Santander");
        listOfBanks.add("Banco Republica");
        listOfBanks.add("Itau");
        listOfBanks.add("Paypal");

        for(int i=0;i<100;i++){
            QueueOfPayments.add(new Payment(listOfBanks.get((Math.round((float) Math.random()*10))%3),1111,100,20));
            QueueOfPayments.add(new Payment(listOfBanks.get((Math.round((float) Math.random()*10))%3),1111,100,30));
            QueueOfPayments.add(new Payment(listOfBanks.get((Math.round((float) Math.random()*10))%3),0000,100,i));
        }

        int totalNumberOfPayments = QueueOfPayments.size();
        ExecutorService paymentProcessor = Executors.newFixedThreadPool(100);


        Runnable runnableTask = () -> {
            ProcesadorDePagos proc= new ProcesadorDePagos();
            Payment payment = QueueOfPayments.poll();
            payment = proc.process(payment);
            QueueOfProcessedPayments.add(payment);

            System.out.println(QueueOfPayments.size());
        };
        int size = QueueOfPayments.size();

        while(size!=0) {
            size--;
            paymentProcessor.execute(runnableTask);
            if(size == 0){
                paymentProcessor.shutdown();
            }
        }

        ExecutorService paymentEmpaquetado = Executors.newFixedThreadPool(100);

        Runnable runnableTask2 = () -> {
            Empaquetado proc= new Empaquetado();
            Payment payment = QueueOfProcessedPayments.poll();
            payment = proc.empaquetar(payment);
            QueueOfPackedPayments.add(payment);
            System.out.println("empaquetados: "+QueueOfPackedPayments.size());
        };

        int copiado = totalNumberOfPayments;
        while(totalNumberOfPayments!=0) {
            if(QueueOfProcessedPayments.size()==0){
                break;
            }
            paymentEmpaquetado.execute(runnableTask2);
            if(totalNumberOfPayments==0){
                paymentEmpaquetado.shutdown();
            }
            totalNumberOfPayments--;
        }

        ExecutorService paymentEnviado = Executors.newFixedThreadPool(100);

        Runnable runnableTask3 = () -> {
            Envio proc= new Envio();
            Payment payment = QueueOfPackedPayments.poll();
            payment = proc.enviar(payment);
            listOfFinishedPayments.add(payment);
            System.out.println("enviados: "+listOfFinishedPayments.size());
        };

        while(copiado!=0) {
            if (QueueOfPackedPayments.size() == 0) {
                break;
            }
            paymentEnviado.execute(runnableTask3);
            copiado--;
        }

        while(true){
            System.out.println(listOfFinishedPayments.size());
            if(listOfFinishedPayments.size()==300){
                paymentProcessor.shutdown();
                paymentEmpaquetado.shutdown();
                paymentEnviado.shutdown();
                System.out.println("final enviado: "+listOfFinishedPayments.get(0).isEnviado());
                System.out.println("final procesado: "+listOfFinishedPayments.get(0).isProcessed());
                break;
            }
        }

    }
}