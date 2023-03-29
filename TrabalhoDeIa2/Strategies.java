import java.util.*;

public class Strategies {
	private static int bestColumn, rootDepth;

	static int minimax(int depth, Board board) {
		rootDepth = depth-1;
		maxValue(depth-1, board);
		return bestColumn;
	}

	static int maxValue(int depth, Board board) {
		if (depth == 0) return board.evaluate();
		int value = Integer.MIN_VALUE; // constante da classe Integer
		Map<Board, Integer> successors = board.successors(Board.YELLOW);
		for (Board successor : successors.keySet()) {
			int value2 = minValue(depth-1, successor);	
			if (value2 > value) {
				value = value2;
				// se (value2 > value) bestColumn é atualizado mas somente depois de ser feito backtrack e estiver na root, por isso a condição: if depth == rootDepth
				if (depth == rootDepth) bestColumn = successors.get(successor).intValue(); // get() retorna um Integer é preciso converter para int
			}
		}
		return value;
	}

	static int minValue(int depth, Board board) {
		if (depth == 0) return board.evaluate();
		int value = Integer.MAX_VALUE; // constante da classe Integer
		Map<Board, Integer> successors = board.successors(Board.RED);
		for (Board successor : successors.keySet()) {
			int value2 = maxValue(depth-1, successor);
			if (value2 < value)
				value = value2;
		}
		return value;
	}
}