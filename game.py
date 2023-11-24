
from turtle import color
import pygame as pg
from dragger import Dragger
from const import *
from board import *
from piece import *
class Game:
    def __init__(self):
        self.board=Board()
        self.dragger=Dragger()

    def show_bg(self,surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (col+row)%2==0:
                    color=(234,235,200)
                else:
                    color=(119,154,88)
                rect=(col* SQSIZE,row*SQSIZE,SQSIZE,SQSIZE)
                pg.draw.rect(surface,color,rect)
                
    def show_pieces(self,surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece=self.board.squares[row][col].piece
                    if piece != self.dragger.piece:
                        piece.set_texture(80)
                        img=pg.image.load(piece.texture)
                        imgcenter=col*SQSIZE+SQSIZE//2,row*SQSIZE+SQSIZE//2
                        piece.texture_rect=img.get_rect(center=imgcenter)
                        surface.blit(img,piece.texture_rect)

    def show_moves(self,surface):
        if self.dragger.dragging:
            piece =self.dragger.piece

            for move in piece.moves:
                color="#C86464" if (move.final.row + move.final.col)% 2 ==0 else "C84646"
                rect =(move.final.col * SQSIZE, move.final.row *SQSIZE,SQSIZE,SQSIZE)
                pg.draw.rect(surface,color,rect)
                
                   