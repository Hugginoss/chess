import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci("stockfish")

board = chess.Board()
board.push_san("Nf3")

result = engine.play(board, chess.engine.Limit(time=1))
print("Best move: ", result.move)

engine.quit()
