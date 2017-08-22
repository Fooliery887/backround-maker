from Fooliery_Framework import *
import os

button_1 = 'Images/keep/Magic_button_green.png'
button_1h = 'Images/keep/Magic_button_blue.png'
button_1c = 'Images/keep/Magic_button_yellow.png'
class Game:
    def __init__(self):
        
        pygame.init()
        self.tilesize = 30
        self.screen = pygame.display.set_mode((wth + 200,hgt+200))
        pygame.display.set_caption(title)
        self.running = True
        self.playing  = True
        self.mpos = pygame.mouse.get_pos()
        self.text_function = Text(self)

        self.clock = pygame.time.Clock()
        
        self.defcheck = Text(self).default 
        self.small_font = pygame.font.Font(None,20)
        self.blank = 0
        self.start_screen()

        self.file_count = 0
        #self.appender = craft
        self.save_files = ['img_save_001.png',
                           'img_save_002.png',
                           'img_save_003.png',
                           'img_save_004.png',
                           'img_save_005.png',
                           'img_save_006.png',
                           'img_save_007.png',
                           'img_save_008.png',
                           'img_save_009.png',
                           'img_save_010.png',
                           'img_save_011.png',]
        for i in craft:
            i.convert()
            i.set_colorkey(black)
        
  
        self.all_sprites = pygame.sprite.Group()
        self.grids = pygame.sprite.Group()
        self.click_check = False
        
        self.size_switch = 0
        self.mousefill_image = 0
        self.drawgrid = True
        self.grid_back = pygame.image.load('Images/keep/grid_back.png')
        self.saved_it = False
        self.sample = pygame.image.load('Images/keep/sample.png')
        
    def new(self):
        self.file_appender()
        print(self.tilesize)
        button_1 = 'keep/Magic_button_green.png'
        button_1h = 'keep/Magic_button_blue.png'
        button_1c = 'keep/Magic_button_yellow.png'
        back_of = 'keep/grid_back.png'
        self.back_of = Surf2(self,self.grid_back,0,0,wth,hgt)
        self.grids.add(self.back_of)
        self.s = Scene(self,craft)
        #print('craft: '+ str(craft))
        self.button1 = Buttons(self,button_1,button_1h,button_1c,wth + (self.tilesize*2) , hgt // 8)
        self.button2 = Buttons(self,button_1,button_1h,button_1c,wth + (self.tilesize*2) , hgt // 4)
        self.button3 = Buttons(self,button_1h,button_1c,button_1,wth + (self.tilesize*2) , hgt // 2)
        try:
            self.all_sprites.add(self.button1)
        except:
            pass
        try:
            self.all_sprites.add(self.button2)
        except:
            pass
        try:
            self.all_sprites.add(self.button3)
        except:
            pass
        

        
        self.grid = Grid(self)
      
        self.mousefill = build_with_click(self,self.tilesize,self.s)
        self.this = pygame.image.load(craft[self.mousefill_image])
        self.this = pygame.transform.scale(self.this,(self.tilesize,self.tilesize))
        self.run()
        

    def update(self):
        self.mpos = pygame.mouse.get_pos()
      
        
        
    def run(self):
        while self.playing:
            self.clock.tick(fps)
            self.events()
            self.draw()
            self.update()
            



    def events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                self.click_check = True
               
                
                self.mousefill.place_tile_sprite()
                
                
                try: 
                    self.button1.button_events_mousedown(self.button1)
                    if self.button1.button_is_clicked(self.button1):
                        self.mousefill_image += 1
                        self.this = pygame.image.load(craft[self.mousefill_image])
                        self.this = pygame.transform.scale(self.this,(self.tilesize,self.tilesize))
                        #print('image number is: ' + self.mousefill_image)
                except:
                    pass
                try: 
                    self.button3.button_events_mousedown(self.button3)
                    if self.button3.button_is_clicked(self.button3):
                        if self.drawgrid == True:
                            self.drawgrid = False
                        elif self.drawgrid == False:
                            self.drawgrid = True
                        
                except:
                    pass
                try:
                    self.button2.button_events_mousedown(self.button2)
                    if self.button2.button_is_clicked(self.button2):
                        self.mousefill_image -= 1
                        self.this = pygame.image.load(craft[self.mousefill_image])
                        self.this = pygame.transform.scale(self.this,(self.tilesize,self.tilesize))
                        #print('image number is: ' + self.mousefill_image)
                except:
                    pass
                    
            if e.type == pygame.MOUSEBUTTONUP:
                self.click_check = False
                try:
                    self.grid.print_mousepos_grid()
                except:
                    pass
                
                try: 
                    self.button1.button_events_mouseup(self.button1)
                except:
                    pass
                try:
                    self.button2.button_events_mouseup(self.button2)
                except:
                    pass
                try:
                    self.button3.button_events_mouseup(self.button3)
                except:
                    pass
           
            
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_p:
                    self.saved_it =True
                    pygame.image.save(self.back_of.image,self.save_files[self.file_count])
                    #print('image saved as :' + str(self.file_count))
                    pygame.time.wait(100)
                    self.preview = pygame.image.load(self.save_files[self.file_count])
                    self.preview = pygame.transform.scale(self.preview, (100,100))
                    self.file_count += 1
                    
                if e.key == pygame.K_z:
                    try:
                        self.mousefill_image += 1
                        self.this = pygame.image.load(craft[self.mousefill_image])
                        self.this = pygame.transform.scale(self.this,(self.tilesize,self.tilesize))
                    except:
                        pass
                if e.key == pygame.K_x:
                    try:
                        self.mousefill_image -= 1
                        self.this = pygame.image.load(craft[self.mousefill_image])
                        self.this = pygame.transform.scale(self.this,(self.tilesize,self.tilesize))
                    except:
                        pass
    
    def draw(self):
        self.screen.fill(black)
        #self.screen.blit(self.grid_back,(8,8))

        Text(self).draw_text2(self.defcheck,'image number : ' + str(self.mousefill_image),purple,(wth // 2)+100, hgt + 100)
        Text(self).draw_text2(self.defcheck,'key_z --> | key_x <-- ' ,purple,(wth // 2)+100, hgt + 130)
        Text(self).draw_text2(self.small_font,'-key_p- to save (.png)',pumpkin,75,hgt + 175)
        Text(self).draw_text2(self.small_font,'scroll up',pumpkin,wth + 150, 65)
        Text(self).draw_text2(self.small_font,'scroll down',pumpkin,wth + 150,130)
        Text(self).draw_text2(self.small_font,'grid toggle',pumpkin,wth + 150,255)
        if self.drawgrid:
            self.grid.draw_grid()
        try:
            self.grid.fill(blurple)
        except:
            pass

        try:
            self.button1.button_scene()
        except:
            pass
        try:
            self.button2.button_scene()
        except:
            pass
        try:
            #print(str(len(self.mousefill.s.list)))
            if self.mousefill_image > len(self.mousefill.s.list):
                self.mousefill_image = 0
            elif self.mousefill_image < 0:
                self.mousefill_image = len(self.mousefill.s.list) - 1
            self.mousefill.fill(self.mousefill_image)
        except:
            pass
        
            #print('blit')
        try:
            
            self.screen.blit(self.this,(wth + 100,hgt + 100))
        except:
            pass
        
    
        if self.saved_it:
            
            try:
                self.screen.blit(self.preview,(10,hgt + 10 ))
            except:
                pass
        else:
            self.screen.blit(self.sample,(10,hgt + 10))
        
            
        self.all_sprites.update()
        self.grids.update()
        self.all_sprites.draw(self.screen)
        self.grids.draw(self.screen)
        self.all_sprites.draw(self.back_of.image)
        pygame.display.flip()

    def start_screen(self):
        did_click = False
        start_display = pygame.sprite.Group()
        self.button_one = Buttons(self,button_1,button_1h,button_1c, wth + 50, hgt // 8)
        self.button_two = Buttons(self,button_1,button_1h,button_1c, wth + 50, hgt // 5)
        start_display.add(self.button_one)
        start_display.add(self.button_two)
        running = True
        while running:
            self.screen.fill(black)
            
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                    self.running = False
                if e.type == pygame.KEYUP:
                    running = False
                if e.type == pygame.MOUSEBUTTONDOWN:
                    self.click_check = True
                    print('clicked')
                    
                    self.button_one.button_events_mousedown(self.button_one)
                    if self.button_one.button_is_clicked(self.button_one):
                        print('start screen button one is pressed')
                        self.tilesize += 1
                    self.button_two.button_events_mousedown(self.button_two)
                    if self.button_two.button_is_clicked(self.button_two):
                        print('start screen button two is pressed')
                        self.tilesize -= 1
                if e.type == pygame.MOUSEBUTTONUP:
                    self.click_check = False
                    self.button_one.button_events_mouseup(self.button_one)
                    self.button_two.button_events_mouseup(self.button_two)
            self.mpos = pygame.mouse.get_pos()        
            self.text_function.draw_text2(self.small_font,'Fooliery EZ Tile',pumpkin,300,300)
            self.text_function.draw_text2(self.small_font,'Increase Tile Size',pumpkin,wth + 120, hgt // 8)
            self.text_function.draw_text2(self.small_font,'Decrease Tile Size',pumpkin,wth + 120, hgt // 5)
            self.text_function.draw_text2(self.small_font,'Current tile size is:  ' + str(self.tilesize),pumpkin,300,330)
            start_display.draw(self.screen)
            start_display.update()
            pygame.display.flip()
    def file_appender(self):
        os.chdir("Images")
        for dirname,dirnames, filenames in os.walk('.'):
            quicklist = []
            if dirname == '.':
                for filename in filenames:
                    #print(os.path.join(filename))
                    craft.append(filename)
                    

g = Game()
while g.running:
    
    g.new()
    g.run()
pygame.quit()
quit()
