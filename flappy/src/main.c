#include "raylib.h"

// user defined
#include "header/declerations.h"

int main()
{
    int screenWidth = 800;
    int screenHeight = 450;

    // Initialization
    SetConfigFlags(FLAG_MSAA_4X_HINT);
    InitWindow(screenWidth, screenHeight, "Flappy Square");

    // music
    startMusic();

    int tmp = 0;
    PlayerStatus player = getPlayerStatus();

    while (tmp != -1)
    {
        tmp = UIWindow(player);
        player = getPlayerStatus();

        if (tmp == 0)
        {
            player = gameWindow(0, player.prefferedShape, player.prefferedTheme);
            if (player.points >= 0)
            {
                saveHighScore(player);
            }
            else
            {
                tmp = -1;
            }
        }
        else if (tmp == 1)
        {
            player = gameWindow(1, player.prefferedShape, player.prefferedTheme);
            saveHighScore(player);
        }
    }

    // De-Initialization
    stopMusic();
    CloseWindow();

    return 0;
}
