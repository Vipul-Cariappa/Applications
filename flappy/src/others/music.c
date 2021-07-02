#include "raylib.h"

Music music;

void startMusic()
{
    InitAudioDevice();
    music = LoadMusicStream("resources/music1.wav");
    PlayMusicStream(music);
    SetMasterVolume(1.0f);
}

void stopMusic()
{
    UnloadMusicStream(music);
    CloseAudioDevice();
}

void updateMusic()
{
    UpdateMusicStream(music);
}
