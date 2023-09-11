import java.util.Base64;
import java.util.Scanner;

// 
// Decompiled by Procyon v0.5.36
// 

class CoffeeShop
{
    public static void failure() {
        System.out.println("Sorry! You didn't get it right...");
    }
    
    public static void success() {
        System.out.println("Nice! You got it!");
        System.out.println("Submit the name you entered inside CACI{} to get points!");
    }
    
    public static void main(final String[] array) {
        final Scanner scanner = new Scanner(System.in);
        System.out.println("What's my name?");
        final String encodeToString = Base64.getEncoder().encodeToString(scanner.nextLine().getBytes());
        if (encodeToString.length() != 20) {
            failure();
        }
        else if (!encodeToString.endsWith("NoZXI=")) {
            failure();
        }
        else if (!encodeToString.startsWith("R2FsZU")) {
            failure();
        }
        else if (!encodeToString.substring(6, 14).equals("JvZXR0aW")) {
            failure();
        }
        else {
            success();
        }
    }
}
//CACI{GaleBoetticher}