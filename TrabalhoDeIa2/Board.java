import java.util.Arrays;

public class Board {
	final char EMPTY = '.';
	final int[] UNSUCCESS = {-1, -1};
	private boolean thereIsAWinner = false;
	private char winner;
	private char[][] board;

	Board(){
		board = new char[6][7];
		for(char[] row : board) Arrays.fill(row, '.');
	}
	
	// coloca uma peça numa coluna; devolve o slot na qual a peça foi colocada se teve êxito, {-1, -1} caso contrario
	public int[] put(int colNumber, char token) {
		for (int i = board.length-1; i >= 0; i--)
			if (board[i][colNumber] == EMPTY) {
				board[i][colNumber] = token;
				return new int[] {i, colNumber};
			}
		return UNSUCCESS;
	}

	// retorna true se o tabuleiro estiver cheio ou false caso contrario
	public boolean isFull(){
		for (int i = 0; i<board[0].length; i++)
			if (board[0][i] == EMPTY) return false;
		return true;
	}

	// recebe um array com coordenadas x, y e verifica se não ha 4 peças alinhadas(horizontal, vertical, ou diagonal) a partir desse slot
	public void verify(int[] slot) {
		if (slot.equals(UNSUCCESS)) return;
		int x = slot[1], y = slot[0]; // coluna: slot[1]; linha: slot[0]
		verify(x, y, 1, 0); verify(x, y, -1, 0); 	 // horizontal
		verify(x, y, 1, -1); verify(x, y, -1, -1); // diagonais (direções SE, SO)
		verify(x, y, 1, 1); verify(x, y, -1, 1); 	 // diagonais (direções NE, NO) 
		verify(x, y, 0, -1); // vertical (da peça para baixo)
	}

	public void verify(int x, int y, int incx, int incy) {
		try {
			for (int i=0, yy=y, xx=x; i<4; i++, xx+=incx, yy+=incy)
				if (board[y][x] != board[yy][xx]) return;
			thereIsAWinner = true;
			winner = board[y][x];
		}
		catch (Exception e) {return;}
   }

	public boolean thereIsAWinner() {return thereIsAWinner;}

	public char getWinner() {return winner;}

	// escolhe a melhor jogada usando um dos 3 algoritmos e faz essa jogada 
	// public int[] computerTurn(int algorithm, char token) {
	// 	int colNumber;
	// 	if (algorithm == 1) {
	// 		colNumber = Strategies.minimax(board);
	// 		return put(colNumber, token); // retornar as coordenadas do slot
	// 	}
	// 	//else if ...
	// }

   // Representacao em String do tabuleiro
	public void printBoard() {
		for (int i=0; i < board.length; i++) {
			String str = String.valueOf(board[i]);
			System.out.println(str);
		}
	}
}