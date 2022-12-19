import java.util.Scanner;

public class RainFallAmounts {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Create an empty array of Month objects with a length of 12.
        Month[] months = new Month[12];
        String[] monthName = {"January","February","March","April","May","June","July","August","September","October","November","December"};

        // Prompt the user to enter a rainfall amount for each month.
        for (int i = 0; i < months.length; i++) {
            System.out.print("Please enter the rainfall amount for " + monthName[i] + ": ");




            // Validate the entered amount.
            int amount = -1;
            while (amount < 0) {
                amount = input.nextInt();

                if (amount < 0) {
                    System.out.println("Invalid amount. Try again");
                }
            }

            // Create a new Month object with the entered amount and add it to the array.
            months[i] = new Month(amount);
        }

        // Calculate and print the total rainfall for the year.
        int total = 0;
        for (int i = 0; i < months.length; i++) {
            total += months[i].getAmount();
        }
        System.out.println("Total rainfall for the year: " + total);

        // Calculate and print the average monthly rainfall for the year.
        double average = total / 12.0;
        System.out.printf("Average monthly rainfall for the year: %.02f%n",  average);

        // Determine and print the month with the most rain.
        int max = Integer.MIN_VALUE;
        int maxIndex = 0;
        for (int i = 0; i < months.length; i++) {
            if(max < months[i].getAmount()) {
                max = months[i].getAmount();
                maxIndex = i;
            }
        }
        System.out.println("The month with the most rain: " + monthName[maxIndex]);

        // Determine and print the month with the least rain.
        int min = Integer.MAX_VALUE;
        int minIndex = 0;
        for (int i = 0; i < months.length; i++) {
            if (months[i].getAmount() < min) {
                min = months[i].getAmount();
                minIndex = i;
            }
        }
        System.out.println("The month with the least rain: " + monthName[minIndex]);


    }
}
