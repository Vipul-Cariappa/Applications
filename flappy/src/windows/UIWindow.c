#include "raylib.h"

// user defined
#include "header/declerations.h"

int UIWindow(PlayerStatus player)
{
    int screenWidth = GetScreenWidth();
    int screenHeight = GetScreenHeight();

    // theme / color
    Color backgroundColor, textColor, buttonColor;

    if (player.prefferedTheme == 2)
    {
        backgroundColor = BLACK;
        textColor = WHITE;
        buttonColor = GRAY;
    }
    else if (player.prefferedTheme == 3)
    {
        backgroundColor = RAYWHITE;
        textColor = BLACK;
        buttonColor = WHITE;
    }
    else
    {
        backgroundColor = RAYWHITE;
        textColor = BLACK;
        buttonColor = GRAY;
    }

    bool canQuit = false;

    // 0: new game, -1: exit, 1: extream mode
    int nextWindow = 9;

    const char *newGameText = "Start New Game";
    const char *extreamModeText = "Extream Mode";
    const char *playerInfoText = TextFormat("Points: %i Coins: %i", player.points, player.coins);
    const char *changeThemeText = "Change Theme";

    int newGameTextLength = MeasureText(newGameText, 20);
    int extreamModeTextLength = MeasureText(extreamModeText, 20);
    int playerInfoTextLength = MeasureText(playerInfoText, 20);
    int changeThemeTextLength = MeasureText(changeThemeText, 20);

    Vector2 newGamePos = {
        (screenWidth - newGameTextLength) / 2 - 20,
        screenHeight / 2 - 37};

    Vector2 newGameDimentions = {
        newGameTextLength + 40,
        24};

    Vector2 extreamModePos = {
        (screenWidth - extreamModeTextLength) / 2 - 20,
        screenHeight / 2 - 11};

    Vector2 extreamModeDimentions = {
        extreamModeTextLength + 40,
        24};

    Vector2 changeThemePos = {
        (screenWidth - changeThemeTextLength) / 2 - 20,
        screenHeight - 28};

    Vector2 changeThemeDimentions = {
        changeThemeTextLength + 40,
        24};

    Vector2 playerInfoPos = {
        (screenWidth - playerInfoTextLength) / 2,
        screenHeight / 2 + 13};

    while (!WindowShouldClose())
    {
        // music
        updateMusic();

        if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON))
        {
            canQuit = true;
            Vector2 ballPosition = GetMousePosition();

            if (
                ballPosition.x >= extreamModePos.x &&
                ballPosition.x <= extreamModePos.x + extreamModeDimentions.x &&
                ballPosition.y >= extreamModePos.y &&
                ballPosition.y <= extreamModePos.y + extreamModeDimentions.y)
            {
                nextWindow = 1;
            }

            if (
                ballPosition.x >= newGamePos.x &&
                ballPosition.x <= newGamePos.x + newGameDimentions.x &&
                ballPosition.y >= newGamePos.y &&
                ballPosition.y <= newGamePos.y + newGameDimentions.y)
            {
                nextWindow = 0;
            }

            if (
                ballPosition.x >= changeThemePos.x &&
                ballPosition.x <= changeThemePos.x + changeThemeDimentions.x &&
                ballPosition.y >= changeThemePos.y &&
                ballPosition.y <= changeThemePos.y + changeThemeDimentions.y)
            {
                player.prefferedTheme += 1;
                if (player.prefferedTheme > 3)
                {
                    player.prefferedTheme = 1;
                }

                saveHighScore((PlayerStatus){0, 0, player.prefferedShape, player.prefferedTheme});

                if (player.prefferedTheme == 2)
                {
                    backgroundColor = BLACK;
                    textColor = WHITE;
                    buttonColor = GRAY;
                }
                else if (player.prefferedTheme == 3)
                {
                    backgroundColor = RAYWHITE;
                    textColor = BLACK;
                    buttonColor = WHITE;
                }
                else
                {
                    backgroundColor = RAYWHITE;
                    textColor = BLACK;
                    buttonColor = GRAY;
                }
            }
        }
        if (IsMouseButtonReleased(MOUSE_LEFT_BUTTON) && canQuit && nextWindow != 9)
        {
            return nextWindow;
        }

        // Draw
        BeginDrawing();
        ClearBackground(backgroundColor);

        DrawRectangle(
            newGamePos.x,
            newGamePos.y,
            newGameDimentions.x,
            newGameDimentions.y,
            buttonColor);

        DrawRectangle(
            extreamModePos.x,
            extreamModePos.y,
            extreamModeDimentions.x,
            extreamModeDimentions.y,
            buttonColor);

        DrawRectangle(
            changeThemePos.x,
            changeThemePos.y,
            changeThemeDimentions.x,
            changeThemeDimentions.y,
            buttonColor);

        DrawText(
            newGameText,
            newGamePos.x + 20,
            newGamePos.y + 2,
            20,
            textColor);

        DrawText(
            extreamModeText,
            extreamModePos.x + 20,
            extreamModePos.y + 2,
            20,
            textColor);

        DrawText(
            playerInfoText,
            playerInfoPos.x,
            playerInfoPos.y,
            20,
            textColor);

        DrawText(
            changeThemeText,
            changeThemePos.x + 20,
            changeThemePos.y + 2,
            20,
            textColor);

        EndDrawing();
    }

    return -1;
}
