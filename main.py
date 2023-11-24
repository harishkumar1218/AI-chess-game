from turtle import Screen
import pygame as pg
import sys
from const import *
from game import Game
from dragger import Dragger
from board import Board

class Main:
    def __init__(self):
        pg.init()
        self.screen=pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption("Chess")
        self.game=Game()
        self.dragger=Dragger()
        self.board=Board()

        
    def mainloop(self):
        game=self.game
        screen=self.screen
        dragger=self.dragger
        board=self.board
        while True:
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_pieces(screen)

            if dragger.dragging :
                dragger.update_blit(screen)
            for event in pg.event.get():
                if event.type==pg.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    clicked_row,clicked_col=dragger.y//SQSIZE,dragger.x//SQSIZE

                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece=board.squares[clicked_row][clicked_col].piece
                        board.cal_move(piece,clicked_row,clicked_col)
                        dragger.saveinitial(event.pos)
                        dragger.drag(piece)
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)

                elif event.type==pg.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)
                elif event.type==pg.MOUSEBUTTONUP:
                    dragger.undraf()


                elif event.type==pg.QUIT:
                    pg.quit()
                    sys.exit()
            pg.display.update()
            
main=Main()
main.mainloop()