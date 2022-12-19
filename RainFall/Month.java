public class Month {
    // Private fields to store the month name and the rainfall amount
    private String monthName;
    private int amount;

    // Public constructor that accepts two arguments
    // The first parameter is a String and is used to set the monthName field
    // The second parameter is an int and is used to set the amount field
    public Month(int amount) {
        this.amount = amount;
    }

    // Public accessor method for retrieving the monthName field
    public String getMonthName() {

        return monthName;
    }

    // Public accessor method for retrieving the amount field
    public int getAmount() {

        return amount;
    }
}