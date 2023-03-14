import java.util.Arrays;

public class Board {
	final char EMPTY = '.';
	boolean theresIsAWinner = false;
	private char[][] board;

	Board(){
		board = new char[6][7];
		for(char[] row : board) Arrays.fill(row, '.');
	}

	// coloca uma peça numa coluna, devolve true se teve êxito, false caso contrario
	public boolean put(int cols, char token) {
		for (int i = board.length-1; i >= 0; i--)
			if (board[i][cols] == EMPTY) {
				board[i][cols] = token;
				return true;
			}
		return false;
	}

	// retorna true se o tabuleiro estiver cheio ou false caso contrario
	public boolean isFull(){
		for (int i = 0; i<board[0].length; i++)
			if (board[0][i] == EMPTY) return false;
		return true;
	}

	// Verifica o estado do jogo, se não há um vencedor
	public boolean verify() {
		// ...
		return true;
	}

   // Representacao em String do tabuleiro
	public void printBoard() {
		for (int i=0; i < board.length; i++) {
			String str = String.valueOf(board[i]);
			System.out.println(str);
		}
	}
}