#include "raylib.h"

// user defined
#include "header/declerations.h"


PlayerStatus getPlayerStatus()
{
    int points = LoadStorageValue(0);
    int coins = LoadStorageValue(1);
    int shape = LoadStorageValue(2);
    int theme = LoadStorageValue(3);

    return (PlayerStatus){points, coins, shape, theme};
}

void saveHighScore(PlayerStatus player)
{
    int points = LoadStorageValue(0);
    int coins = LoadStorageValue(1);
    player.coins += coins;

    if (player.points > points)
    {
        SaveStorageValue(0, player.points);
    }
    SaveStorageValue(1, player.coins);
    SaveStorageValue(2, player.prefferedShape);
    SaveStorageValue(3, player.prefferedTheme);
}
