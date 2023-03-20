import java.util.*;

class Ruins {
    public static void main(String[] args) {
        Ruins ruins = new Ruins();

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the ruins password: ");
        String input = scanner.next();
        input = input.substring("vrnctf{".length(),input.length()-1);
        if (ruins.checkPassword(input)) {
            System.out.println("The door opened, but there was nothing behind it! Maybe the treasure is something else?");
        } else {
            System.out.println("Nothing happened");
        }
    }

    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("7r345ur3_u0y_51_dn3_r0_rufy1dn45");
    }
}