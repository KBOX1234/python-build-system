#include "raylib.h"
#include "imgui.h"
#include "rlImGui.h"
#include <enet/enet.h>
#include <iostream>

int main() {
    // Initialize Raylib
    InitWindow(800, 600, "Raylib + ImGui + ENet + librg Demo");
    SetTargetFPS(60);

    // Initialize ImGui (via rlImGui)
    rlImGuiSetup(true);

    // Initialize ENet
    if (enet_initialize() != 0) {
        std::cerr << "An error occurred while initializing ENet.\n";
        return EXIT_FAILURE;
    }
    atexit(enet_deinitialize);

    // Main game loop
    while (!WindowShouldClose()) {
        // Begin drawing
        BeginDrawing();
        ClearBackground(RAYWHITE);

        // Begin ImGui frame
        rlImGuiBegin();

        // ImGui window
        ImGui::Begin("Demo Window");
        ImGui::Text("Hello, Raylib + ImGui + ENet + librg!");
        if (ImGui::Button("Press me")) {
            std::cout << "Button was pressed!" << std::endl;
        }
        ImGui::End();

        // End ImGui frame
        rlImGuiEnd();

        DrawText("Raylib window is running!", 10, 10, 20, DARKGRAY);

        // End drawing
        EndDrawing();
    }

    // Clean up
    rlImGuiShutdown();
    CloseWindow();

    return 0;
}
