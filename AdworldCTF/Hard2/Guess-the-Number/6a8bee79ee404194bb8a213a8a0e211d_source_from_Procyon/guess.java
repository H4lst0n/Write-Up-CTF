import java.math.BigInteger;

public class guess
{
    static String XOR(final String _str_one, final String _str_two) {
        final BigInteger i1 = new BigInteger(_str_one, 16);
        final BigInteger i2 = new BigInteger(_str_two, 16);
        final BigInteger res = i1.xor(i2);
        final String result = res.toString(16);
        return result;
    }
    
    public static void main(final String[] args) {
        int guess_number = 0;
        int my_num = 349763335;
        final int my_number = 1545686892;
        final int flag = 345736730;
        if (args.length > 0) {
            try {
                guess_number = Integer.parseInt(args[0]);
                if (my_number / 5 == guess_number) {
                    final String str_one = "4b64ca12ace755516c178f72d05d7061";
                    final String str_two = "ecd44646cfe5994ebeb35bf922e25dba";
                    my_num += flag;
                    final String answer = XOR(str_one, str_two);
                    System.out.println("your flag is: " + answer);
                }
                else {
                    System.err.println("wrong guess!");
                    System.exit(1);
                }
            }
            catch (NumberFormatException e) {
                System.err.println("please enter an integer \nexample: java -jar guess 12");
                System.exit(1);
            }
        }
        else {
            System.err.println("wrong guess!");
            int num = 1000000;
            ++num;
            System.exit(1);
        }
    }
}
