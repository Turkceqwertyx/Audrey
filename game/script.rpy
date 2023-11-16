# Define Characters
define k = Character("Klein Moretti")
define z = Character("Zhou Mingrui")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show z angry

    z "Painful!"
    z "How painful!"
    z "My head hurts so badly!"

    # This ends the game.

    return
