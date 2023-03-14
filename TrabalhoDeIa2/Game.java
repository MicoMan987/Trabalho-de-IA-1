// copy-paste to compile -> javac Game.java && java Game

import java.util.Scanner;

public class Game {
	final static char YELLOW = 'X';
	final static char RED = 'O';

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		Board board = new Board();
		
		// Testing
		System.out.println("Your turn");
		board.put(in.nextInt(), RED);
		board.printBoard();

		// aqui acontecerá toda a interação entre a máquina e a pessoa que está jogando
		// while (!board.isFull() && !board.theresIsAWinner) {
		// 	System.out.println("Your turn");
		// 	board.put(in.nextInt(), RED);
		// 	board.printBoard();
		// }
	}
}