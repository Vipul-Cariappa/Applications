#ifndef USR_HEADER
#define USR_HEADER

#ifdef __cplusplus
extern "C"
{
#endif

    typedef struct PlayerStatus
    {
        int points;
        int coins;
        int prefferedShape;
        int prefferedTheme;
    } PlayerStatus;

    int UIWindow(PlayerStatus player);
    PlayerStatus gameWindow(int gameMode, int shape, int theme);
    PlayerStatus getPlayerStatus();
    void saveHighScore(PlayerStatus player);
    void startMusic();
    void stopMusic();
    void updateMusic();

#ifdef __cplusplus
}
#endif

#endif // USR_HEADER
