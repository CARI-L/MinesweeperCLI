import java.util.Scanner;

public class MinesweeperCLI {
    public static void main(String[] args) {

        // ",\s*|\s+"
        try {

            Board b = new Board(12, 30);
            b.randomBoard(99);
            System.out.println(b);
            
        } catch (NumberFormatException n) {
            System.out.println("Error! Board parameters provided are not valid.");
        }
    }
    
    static void showCommands(Scanner sys_in) {
        clearScreen();

        System.out.println("==============");
        System.out.println("|| Commands ||");
        System.out.println("==============");
        System.out.println();

        System.out.println("x y");
        System.out.println("x, y");
        System.out.println("(x, y)          dig at space (x, y)");
        System.out.println("flag x y");
        System.out.println("flag x, y");
        System.out.println("flag (x, y)     flag space (x, y)");
        System.out.println();
        System.out.print("Press any key to continue: ");
        sys_in.next();

    }

    static void clearScreen() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }
}