init python:

    def piece_dragged(drags, drop):

        if not drop:
            store.piecelist[(int(drags[0].drag_name[0]) * 10 + int(drags[0].drag_name[1]))][0] = drags[0].x
            store.piecelist[(int(drags[0].drag_name[0]) * 10 + int(drags[0].drag_name[1]))][1] = drags[0].y
            return

        store.movedpiece = int(drags[0].drag_name[0]) * 10 + int(drags[0].drag_name[1])
        store.movedplace = [int(drop.drag_name[0]), int(drop.drag_name[1])]

        return True

screen jigsaw:

    draggroup:

        drag:
            drag_name "00"
            child "empty space.png"
            draggable False
            xpos coorlistx[0] ypos coorlisty[0]

        drag:
            drag_name "01"
            child "empty space.png"
            draggable False
            xpos coorlistx[0] ypos coorlisty[1]

        drag:
            drag_name "02"
            child "empty space.png"
            draggable False
            xpos coorlistx[0] ypos coorlisty[2]

        drag:
            drag_name "10"
            child "empty space.png"
            draggable False
            xpos coorlistx[1] ypos coorlisty[0]

        drag:
            drag_name "11"
            child "empty space.png"
            draggable False
            xpos coorlistx[1] ypos coorlisty[1]

        drag:
            drag_name "12"
            child "empty space.png"
            draggable False
            xpos coorlistx[1] ypos coorlisty[2]

        drag:
            drag_name "20"
            child "empty space.png"
            draggable False
            xpos coorlistx[2] ypos coorlisty[0]

        drag:
            drag_name "21"
            child "empty space.png"
            draggable False
            xpos coorlistx[2] ypos coorlisty[1]

        drag:
            drag_name "22"
            child "empty space.png"
            draggable False
            xpos coorlistx[2] ypos coorlisty[2]

        drag:
            drag_name "30"
            child "empty space.png"
            draggable False
            xpos coorlistx[3] ypos coorlisty[0]

        drag:
            drag_name "31"
            child "empty space.png"
            draggable False
            xpos coorlistx[3] ypos coorlisty[1]

        drag:
            drag_name "32"
            child "empty space.png"
            draggable False
            xpos coorlistx[3] ypos coorlisty[2]

        drag:
            drag_name "00 piece"
            child im.Crop("jigsaw_image.jpg", 0,0, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[0][0] ypos piecelist[0][1]

        drag:
            drag_name "01 piece"
            child im.Crop("jigsaw_image.jpg", 120,0, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[1][0] ypos piecelist[1][1]

        drag:
            drag_name "02 piece"
            child im.Crop("jigsaw_image.jpg", 240,0, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[2][0] ypos piecelist[2][1]

        drag:
            drag_name "03 piece"
            child im.Crop("jigsaw_image.jpg", 360,0, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[3][0] ypos piecelist[3][1]

        drag:
            drag_name "04 piece"
            child im.Crop("jigsaw_image.jpg", 0,207, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[4][0] ypos piecelist[4][1]

        drag:
            drag_name "05 piece"
            child im.Crop("jigsaw_image.jpg", 120,207, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[5][0] ypos piecelist[5][1]

        drag:
            drag_name "06 piece"
            child im.Crop("jigsaw_image.jpg", 240,207, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[6][0] ypos piecelist[6][1]

        drag:
            drag_name "07 piece"
            child im.Crop("jigsaw_image.jpg", 360,207, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[7][0] ypos piecelist[7][1]

        drag:
            drag_name "08 piece"
            child im.Crop("jigsaw_image.jpg", 0,414, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[8][0] ypos piecelist[8][1]

        drag:
            drag_name "09 piece"
            child im.Crop("jigsaw_image.jpg", 120,414, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[9][0] ypos piecelist[9][1]

        drag:
            drag_name "10 piece"
            child im.Crop("jigsaw_image.jpg", 240,414, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[10][0] ypos piecelist[10][1]

        drag:
            drag_name "11 piece"
            child im.Crop("jigsaw_image.jpg", 360,414, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[11][0] ypos piecelist[11][1]


label puzzle:
    call screen jigsaw
    if ([coorlistx[movedplace[0]], coorlisty[movedplace[1]]] in piecelist):
        python:
            t1 = piecelist[movedpiece]
            t2 = piecelist.index([coorlistx[movedplace[0]], coorlisty[movedplace[1]]])
            piecelist[movedpiece] = [coorlistx[movedplace[0]],coorlisty[movedplace[1]]]
            piecelist[t2] = t1
    else:
        $ piecelist[movedpiece] = [coorlistx[movedplace[0]],coorlisty[movedplace[1]]]
    if piecelist == [[coorlistx[0],coorlisty[0]],
                        [coorlistx[1],coorlisty[0]],
                        [coorlistx[2],coorlisty[0]],
                        [coorlistx[3],coorlisty[0]],
                        [coorlistx[0],coorlisty[1]],
                        [coorlistx[1],coorlisty[1]],
                        [coorlistx[2],coorlisty[1]],
                        [coorlistx[3],coorlisty[1]],
                        [coorlistx[0],coorlisty[2]],
                        [coorlistx[1],coorlisty[2]],
                        [coorlistx[2],coorlisty[2]],
                        [coorlistx[3],coorlisty[2]]]:
        return
    jump puzzle

label start_jigsaw:
    scene bg home queryjigsaw
    image whole = "jigsaw_image.jpg"
    python:
        # coorlistx = [10, 130, 250, 370]
        # coorlisty = [10, 217, 424]
        coorlistx = [80, 200, 320, 440]
        coorlisty = [55, 263, 469]
        piecelist = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        for i in range(12):
            x = renpy.random.randint(0, 59) + 621
            y = renpy.random.randint(30, 480)
            piecelist[i] = [x,y]
        movedpiece = 0
        movedplace = [0, 0]
    jump puzzle
