init python:

    def piece_dragged(drags, drop):

        if not drop:
            return

        store.movedpiece = int(drags[0].drag_name[0]) * 10 + int(drags[0].drag_name[1])
        store.movedplace = [int(drop.drag_name[0]), int(drop.drag_name[1])]

        return True

screen parsons_picture_screen:

    draggroup:

        drag:
            drag_name "00"
            child "null empty space.png"
            draggable False
            xpos coorlistx[0] ypos coorlisty[0]

        drag:
            drag_name "01"
            child "null empty space.png"
            draggable False
            xpos coorlistx[1] ypos coorlisty[1]

        drag:
            drag_name "02"
            child "null empty space.png"
            draggable False
            xpos coorlistx[2] ypos coorlisty[2]

        drag:
            drag_name "00 piece"
            child "parsons/04.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[0][0] ypos piecelist[0][1]

        drag:
            drag_name "01 piece"
            child "parsons/01.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[1][0] ypos piecelist[1][1]

        drag:
            drag_name "02 piece"
            child "parsons/05.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[2][0] ypos piecelist[2][1]

        drag:
            drag_name "03 piece"
            child "parsons/02.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[3][0] ypos piecelist[3][1]

        drag:
            drag_name "04 piece"
            child "parsons/06.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[4][0] ypos piecelist[4][1]

        drag:
            drag_name "05 piece"
            child "parsons/03.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[5][0] ypos piecelist[5][1]

        drag:
            drag_name "06 piece"
            child "parsons/07.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[6][0] ypos piecelist[6][1]


label parsons_picture:
    call screen parsons_picture_screen
    if ([coorlistx[movedplace[0]], coorlisty[movedplace[1]]] in piecelist):
        python:
            t1 = piecelist[movedpiece]
            t2 = piecelist.index([coorlistx[movedplace[0]], coorlisty[movedplace[1]]])
            piecelist[movedpiece] = [coorlistx[movedplace[0]],coorlisty[movedplace[1]]]
            piecelist[t2] = t1
    else:
        $ piecelist[movedpiece] = [coorlistx[movedplace[0]],coorlisty[movedplace[1]]]
    $ placelist = [piecelist[1], piecelist[3],piecelist[5]]
    if placelist == [[coorlistx[0],coorlisty[0]],
                        [coorlistx[0],coorlisty[1]],
                        [coorlistx[0],coorlisty[2]]]:
        return
    jump parsons_picture

label start_parsons_pic:
    scene bg home parsons
    python:
        coorlistx = [71, 71, 71]
        coorlisty = [89, 289, 480]
        piecelist = [[490,62],[490,121],[490,182],[490,264],[490,372],[490,476],[490,578]]
        movedpiece = 0
        movedplace = [0, 0]
    jump parsons_picture
