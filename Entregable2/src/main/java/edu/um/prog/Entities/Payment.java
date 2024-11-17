package main.java.com.um.prog.Entities;

public class Payment {
    private String senderBank = "";
    private Integer senderAccountNumber = null;
    private Integer amount = null;
    private Integer priority = 0;
    private boolean empaquetado = false;
    private boolean processed = false;
    private boolean enviado = false;

    public boolean isEnviado() {
        return enviado;
    }

    public void setEnviado(boolean enviado) {
        this.enviado = enviado;
    }

    public Payment(String senderBank, Integer senderAccountNumber, Integer amount, Integer priority) {
        this.senderBank = senderBank;
        this.senderAccountNumber = senderAccountNumber;
        this.amount = amount;
        this.priority = priority;
    }

    public Integer getPriority() {
        return priority;
    }

    public void setPriority(Integer priority) {
        this.priority = priority;
    }

    public Integer getAmount() {
        return amount;
    }

    public void setAmount(Integer amount) {
        this.amount = amount;
    }

    public String getSenderBank() {
        return senderBank;
    }

    public void setSenderBank(String senderBank) {
        this.senderBank = senderBank;
    }




    public Integer getSenderAccountNumber() {
        return senderAccountNumber;
    }

    public void setSenderAccountNumber(Integer senderAccountNumber) {
        this.senderAccountNumber = senderAccountNumber;
    }

    public int compareTo(Payment o) {
        if (this.priority > o.priority) {
            // Current object is older, return 1
            return -1;
        } else if (this.priority < o.priority) {
            // Current object is younger, return -1
            return 1;
        } else {
            // Ages are the same, return 0
            return 0;
        }
    }

    public boolean isProcessed() {
        return processed;
    }

    public void setProcessed(boolean processed) {
        this.processed = processed;
    }

    public boolean isEmpaquetado() {
        return empaquetado;
    }

    public void setEmpaquetado(boolean empaquetado) {
        this.empaquetado = empaquetado;
    }
}
