import pygame as pg
from const import SQSIZE
from piece import *
class Dragger:
    def __init__(self):
        self.x=0
        self.y=0
        self.dragging=False
        self.init_row=0
        self.init_col=0
        self.piece=None

    def update_blit(self,surface):
        self.piece.set_texture(size=128)
        texture=self.piece.texture
        img=pg.image.load(texture)
        img_center=(self.x,self.y)
        self.piece.texture_rect=img.get_rect(center=img_center)
        surface.blit(img,self.piece.texture_rect)

    def update_mouse(self,pos):
        self.x,self.y=pos

    def saveinitial(self,pos):
        self.init_col,self.init_row=pos[0]//SQSIZE,pos[1]//SQSIZE

    def drag(self,piece):
        self.piece=piece
        self.dragging=True

    def undraf(self):
        self.piece=None
        self.dragging=False
