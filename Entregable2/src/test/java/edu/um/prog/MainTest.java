package test.java.com.um.prog;

import main.java.com.um.prog.Entities.Empaquetado;
import main.java.com.um.prog.Entities.Envio;
import main.java.com.um.prog.Entities.Payment;
import main.java.com.um.prog.Entities.ProcesadorDePagos;

import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;
import org.junit.jupiter.api.Test;

public class MainTest {

    @Test
    public void payment(){
        Payment pago = new Payment("Santander",0000,100,20);
        assertFalse(pago.isProcessed());
        ProcesadorDePagos proc = new ProcesadorDePagos();
        proc.process(pago);
        assertTrue(pago.isProcessed());
    }
    @Test
    public void empaquetado(){
        Payment pago = new Payment("Santander",0000,100,20);
        assertFalse(pago.isEmpaquetado());
        Empaquetado proc = new Empaquetado();
        proc.empaquetar(pago);
        assertTrue(pago.isEmpaquetado());
    }
    @Test
    public void enviado(){
        Payment pago = new Payment("Santander",0000,100,20);
        assertFalse(pago.isEnviado());
        Envio proc = new Envio();
        proc.enviar(pago);
        assertTrue(pago.isEnviado());
    }
}
