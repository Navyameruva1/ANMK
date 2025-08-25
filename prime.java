 public class prime{
   public static void main(String[] args) {
   System.out.println("Prime numbers between 1 and 500 are:");

        // Loop through numbers from 2 to 100
        for (int i = 2; i <= 500; i++) {
            if (isPrime(i)) {
                System.out.print(i + " ");
            }
        }
    }

    // Method to check if a number is prime
    public static boolean isPrime(int number) {
        // Numbers less than or equal to 1 are not prime
        if (number <= 1) {
            return false;
        }

        // Check for divisibility from 2 up to the square root of the number
        // This optimization reduces the number of checks needed
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false; // If divisible, it's not prime
            }
        }
        return true; // If no divisors found, it's prime
    }

}

