// copy-paste to compile -> javac Game.java && java Game
import java.util.Scanner;

public class Game {
	static Scanner stdin = new Scanner(System.in);
	static Board board;
	static int strategy; // um número escolhido pelo usário; representa um dos 3 algoritmos

	public static void sayWhoIsTheWinner() {
		if (board.thereIsAWinner()) {
			if (board.getWinner() == Board.YELLOW)
				System.out.println("------ THE WINNER IS PLAYER '" + board.getWinner() + "', YOU LOSE! ------");
			else
				System.out.println("------ THE WINNER IS PLAYER '" + board.getWinner() + "', YOU WIN! ------");
		}
		else System.out.println("------ THE GAME ENDED IN A DRAW! ------");
	}

	public static void chooseStrategy() {
		System.out.println("Choose a strategy: 1 - MINIMAX, 2 - ALPHA-BETA, 3 - MCTS");
		System.out.print("Insert a number:");
		strategy = stdin.nextInt();
	}

	public static void main(String[] args) {
		board = new Board();
		chooseStrategy();
		// aqui acontecerá toda a interação entre a máquina e a pessoa que está jogando
		board.printBoard();
		while (!board.isFull() && !board.thereIsAWinner()) {
			int column = board.computerTurn(strategy, Board.YELLOW);
			System.out.printf("\nComputer move: %d\n\n", column);
			board.check();
			if (board.thereIsAWinner()) break; // se houve um vencedor sai do ciclo
			board.printBoard();
			System.out.println("0123456");
			System.out.println("\nYour turn, choose a column number");
			while(!board.put(stdin.nextInt(), Board.RED))
				System.out.println("This column is full, choose another one.");
			board.check();
		}
		board.printBoard();
		sayWhoIsTheWinner();
	}
}