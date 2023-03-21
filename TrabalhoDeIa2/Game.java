// copy-paste to compile -> javac Game.java && java Game
import java.util.Scanner;

public class Game {
	final static char YELLOW = 'X';
	final static char RED = 'O';
	static Scanner stdin = new Scanner(System.in);
	static Board board;
	static int algorithm; // um número escolhido pelo usário; representa um dos 3 algoritmos

	public static void sayWhoIsTheWinner() {
		if (board.thereIsAWinner()) System.out.println("------ THE WINNER IS PLAYER '" + board.getWinner() + "'! ------");
		else System.out.println("------ THE GAME ENDED IN A DRAW! ------");
	}

	public static void chooseAlgorithm() {
		System.out.println("Choose an algorithm: 1 - MINIMAX, 2 - ALPHA-BETA, 3 - MCTS");
		System.out.print("Insert a number:");
		algorithm = stdin.nextInt();
	}

	public static void main(String[] args) {
		board = new Board();
		// chooseAlgorithm();

		// aqui acontecerá toda a interação entre a máquina e a pessoa que está jogando
		int[] slot = new int[2];
		while (!board.isFull() && !board.thereIsAWinner()) {
			board.printBoard();
			System.out.println("\n0123456");
			System.out.println("'O' turn\n");
			slot = board.put(stdin.nextInt(), RED);
			board.verify(slot);
			if (board.thereIsAWinner()) break; // se o RED venceu sai do ciclo
			board.printBoard();
			System.out.println("\n0123456");
			System.out.println("'X' turn\n");
			slot = board.put(stdin.nextInt(), YELLOW);
			board.verify(slot);
		}
		board.printBoard();
		sayWhoIsTheWinner();
	}
}

// while (!board.isFull() && !board.thereIsAWinner()) {
// 	board.printBoard();
// 	System.out.println("0123456");
// 	System.out.println("Your turn");
// 	slot = board.put(stdin.nextInt(), RED);
// 	board.verify(slot);
// 	if (board.thereIsAWinner()) break; // se o humano venceu sai do ciclo
// 	slot = board.computerTurn(algorithm, YELLOW);
// 	board.verify(slot);
// }