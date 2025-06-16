import java.util.Scanner;

public class MinesweeperCLI {
    public static void main(String[] args) {

        // ",\s*|\s+"

        Board b = new Board(9);
        b.randomBoard(10);
        System.out.println(b);
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