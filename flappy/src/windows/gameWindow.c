#include "raylib.h"

// user defined
#include "header/declerations.h"

void updateCamera(Camera2D *camera, Vector2 playerPos, float delta, int width, int height);

// gameMode: 0 normal; 1 extream mode
// shape: 1 rectangle; 2 circle; 3 triangle
// theme: 1 normal; 2 dark; 3 light; 4 rainbow
PlayerStatus gameWindow(int gameMode, int shape, int theme)
{
    int screenWidth = GetScreenWidth();
    int screenHeight = GetScreenHeight();

    // theme / color
    Color backgroundColor, playerColor, objColor;

    if (theme == 2)
    {
        backgroundColor = BLACK;
        playerColor = WHITE;
        objColor = WHITE;
    }
    else if (theme == 3)
    {
        backgroundColor = RAYWHITE;
        playerColor = BLACK;
        objColor = BLACK;
    }
    else
    {
        backgroundColor = RAYWHITE;
        playerColor = BLUE;
        objColor = GREEN;
    }

    // Ground Rectangle
    Rectangle ground = {0, (float)screenHeight, (float)screenWidth, 20};

    // Player Rectangle
    Rectangle player = {((float)screenWidth / 2) - 100, (float)screenHeight / 2, 25, 25};
    int playerPoints = 0;
    int coinsCount = 0;
    float deltaX = 0;

    // obstacles init
    int o1 = GetRandomValue(150, screenHeight - 150);
    int o2 = GetRandomValue(150, screenHeight - 150);
    int o3 = GetRandomValue(150, screenHeight - 150);
    int o4 = GetRandomValue(150, screenHeight - 150);
    int o5 = GetRandomValue(150, screenHeight - 150);
    int o6 = GetRandomValue(150, screenHeight - 150);

    // Obstacles subjects
    Rectangle objects[] = {
        (Rectangle){(float)screenWidth / 2 + 100, -500, 100, o1 + 500},
        (Rectangle){(float)screenWidth / 2 + 100, o1 + 100, 100, screenHeight - o1 + 400},
        (Rectangle){(float)screenWidth / 2 + 400, -500, 100, o2 + 500},
        (Rectangle){(float)screenWidth / 2 + 400, o2 + 100, 100, screenHeight - o2 + 400},
        (Rectangle){(float)screenWidth / 2 + 700, -500, 100, o3 + 500},
        (Rectangle){(float)screenWidth / 2 + 700, o3 + 100, 100, screenHeight - o3 + 400},
        (Rectangle){(float)screenWidth / 2 + 1000, -500, 100, o4 + 500},
        (Rectangle){(float)screenWidth / 2 + 1000, o4 + 100, 100, screenHeight - o4 + 400},
        (Rectangle){(float)screenWidth / 2 + 1300, -500, 100, o5 + 500},
        (Rectangle){(float)screenWidth / 2 + 1300, o5 + 100, 100, screenHeight - o5 + 400},
        (Rectangle){(float)screenWidth / 2 + 1600, -500, 100, o6 + 500},
        (Rectangle){(float)screenWidth / 2 + 1600, o6 + 100, 100, screenHeight - o6 + 400},
    };

    int objectLength = sizeof objects / sizeof objects[0];

    // Coins
    int c1 = GetRandomValue(150, screenHeight - 150);
    int c2 = GetRandomValue(150, screenHeight - 150);
    int c3 = GetRandomValue(150, screenHeight - 150);
    int c4 = GetRandomValue(150, screenHeight - 150);
    int c5 = GetRandomValue(150, screenHeight - 150);
    int c6 = GetRandomValue(150, screenHeight - 150);

    Vector2 coins[] = {
        (Vector2){screenWidth / 2 + 300, c1},
        (Vector2){screenWidth / 2 + 600, c2},
        (Vector2){screenWidth / 2 + 900, c3},
        (Vector2){screenWidth / 2 + 1200, c4},
        (Vector2){screenWidth / 2 + 1500, c5},
        (Vector2){screenWidth / 2 + 1800, c6},
    };

    bool coinCollected[] = {
        false,
        false,
        false,
        false,
        false,
        false,
    };

    int coinLength = sizeof coins / sizeof coins[0];

    // game info
    float objSpeed = 100.0f;
    bool gameOver = false;

    // physics
    float acclerationY = 300.0f;
    float velocityY = 00.0f;

    // camera
    Camera2D camera = {0};
    camera.target = (Vector2){player.x, player.y};
    camera.offset = (Vector2){screenWidth / 2.0f, screenHeight / 2.0f};
    camera.rotation = 0.0f;
    camera.zoom = 1.0f;

    // Main game loop
    while (!WindowShouldClose())
    {
        // music
        updateMusic();

        // Time
        float deltaTime = GetFrameTime();

        // Update

        // keyboard events
        if (gameOver)
        {
            if (IsKeyPressed(KEY_SPACE))
            {
                return (PlayerStatus){playerPoints, coinsCount, shape, theme};
            }
            if (IsMouseButtonReleased(MOUSE_LEFT_BUTTON))
            {
                return (PlayerStatus){playerPoints, coinsCount, shape, theme};
            }
        }

        if (IsKeyDown(KEY_SPACE))
        {
            acclerationY = -600.0f;
        }
        else if (IsMouseButtonDown(MOUSE_LEFT_BUTTON))
        {
            acclerationY = -600.0f;
        }
        else
        {
            acclerationY = 300.0f;
        }

        // calculate position and velocity
        velocityY += acclerationY * deltaTime;

        if (!CheckCollisionRecs(ground, player))
        {
            velocityY += acclerationY * deltaTime;
            player.y += velocityY * deltaTime + 0.5 * acclerationY * deltaTime * deltaTime;
        }
        else
        {
            velocityY = 0;
            objSpeed = 0;
            gameOver = true;
        }

        if (player.y < 0)
        {
            objSpeed = 0;
            gameOver = true;
        }

        // obstacles building
        for (int i = 0; i < objectLength; i++)
        {
            if (gameMode)
            {
                objects[i].x -= objSpeed * deltaTime + 0.5f * 10.0f * deltaTime * deltaTime;
            }
            else
            {
                objects[i].x -= objSpeed * deltaTime;
            }

            // executes once in two iteration
            if (i % 2 == 0)
            {
                if (objects[i].x < -300)
                {
                    int o = GetRandomValue(150, screenHeight - 150);

                    objects[i].x = (float)screenWidth / 2 + 1100;
                    objects[i + 1].x = (float)screenWidth / 2 + 1100;

                    objects[i].height = o + 500;
                    objects[i + 1].height = screenHeight - o + 400;

                    objects[i + 1].y = o + 100;
                }

                // check collision
                if (CheckCollisionRecs(player, objects[i]) || CheckCollisionRecs(player, objects[i + 1]))
                {
                    objSpeed = 0;
                    gameOver = true;
                }
            }
        }

        for (int i = 0; i < coinLength; i++)
        {
            if (CheckCollisionCircleRec(coins[i], 10, player) && !coinCollected[i])
            {
                coinCollected[i] = true;
                coinsCount += 1;
            }

            if (coins[i].x < -300)
            {
                int o = GetRandomValue(150, screenHeight - 150);
                coins[i].x = screenWidth / 2 + 1100;
                coins[i].y = o;
                coinCollected[i] = false;
            }
            if (gameMode)
            {
                coins[i].x -= objSpeed * deltaTime + 0.5f * 10.0f * deltaTime * deltaTime;
            }
            else
            {
                coins[i].x -= objSpeed * deltaTime;
            }
        }

        deltaX += objSpeed * deltaTime;

        if (deltaX >= 300)
        {
            deltaX = 0;
            playerPoints += 1;
        }

        // camera update
        if (gameMode)
        {
            updateCamera(&camera, (Vector2){player.x, player.y}, deltaTime, screenWidth, screenHeight);
        }

        // Draw
        BeginDrawing();

        ClearBackground(backgroundColor);

        BeginMode2D(camera);

        // -------- coins -------
        for (int i = 0; i < coinLength; i++)
        {
            if (!coinCollected[i])
            {
                DrawCircleV(coins[i], 10, GOLD);
            }
        }
        // ----------------------

        DrawRectangleRec(player, playerColor); // player

        // walls
        for (int i = 0; i < objectLength; i++)
        {
            DrawRectangleRec(objects[i], objColor);
        }

        EndMode2D();

        DrawText(
            TextFormat("Points: %i", playerPoints),
            (screenWidth - MeasureText(TextFormat("Points: %i", playerPoints), 20)) / 2,
            0,
            20,
            GRAY);

        DrawText(
            TextFormat("Coins: %i", coinsCount),
            (screenWidth - MeasureText(TextFormat("Coins: %i", coinsCount), 20)) / 2,
            24,
            20,
            GRAY);

        if (gameOver)
        {
            DrawText(
                "Game Over",
                (screenWidth - MeasureText("Game Over", 20)) / 2,
                screenHeight / 2,
                20,
                GRAY);
        }

        DrawFPS(0, 0);

        EndDrawing();
        //----------------------------------------------------------------------------------
    }

    return (PlayerStatus){-1, -1, -1, -1};
}

float timeKeep = 0;
int rotationDirection = 1;

void updateCamera(Camera2D *camera, Vector2 playerPos, float delta, int width, int height)
{
    // camera->offset = (Vector2){ width/2.0f, height/2.0f };
    // camera->target = playerPos;
    if (timeKeep < 3)
    {
        timeKeep += delta;
    }
    else
    {
        timeKeep = 0;
        rotationDirection = GetRandomValue(0, 1);
    }

    if (rotationDirection)
    {
        camera->rotation -= delta * 2;
    }
    else
    {
        camera->rotation += delta * 2;
    }
}
