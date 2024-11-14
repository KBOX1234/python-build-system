import os
import platform

flags = ""

os.system('mkdir dep')
os.system('git clone https://github.com/raylib-extras/rlImGui.git ./dep/rlImGui')
os.system('curl -L https://github.com/zpl-c/librg/releases/latest/download/librg.h > ./dep/librg.h')
os.system('git clone https://github.com/lsalzman/enet.git ./dep/enet')
os.system('git clone https://github.com/ocornut/imgui.git ./dep/imgui')
os.system('git clone https://github.com/raysan5/raylib.git ./dep/raylib')

# Check for Windows
if platform.system() == 'Windows':
    print("Setting up for windows")

    os.chdir('./dep/rlImGui/')
    os.system('./premake5.exe --cc gcc --clean --gmake')
    os.system('make')
    os.chdir('../../')

# Check for Linux
elif platform.system() == 'Linux':
    print("Setting up for linux")
    os.chdir('./dep/rlImGui/')
    os.system('chmod +x ./premake5')
    os.system('./premake5 --cc=gcc gmake')
    os.system('make')
    os.chdir('../../')

# Check for macOS
elif platform.system() == 'Darwin':
    print("Setting up for MacOSX")

    os.chdir('./dep/rlImGui/')
    os.system('./premake5.osx --cc gcc --clean --gmake')
    os.system('make')
    os.chdir('../../')
else:
    print("Unknown Platform")
    print("failed to set up")
    exit(-1)

#os.chdir('./dep/raylib/src')
#os.system('make')
#os.chdir('../../..')

os.chdir('./dep/enet/')
os.system('cmake CMakeLists.txt')
os.system('make')
os.chdir('../..')

os.system('mkdir ./dep/complib')
os.system('cp ./dep/rlImGui/bin/Debug/libraylib.a ./dep/complib/')
os.system('cp ./dep/rlImGui/bin/Debug/librlImGui.a ./dep/complib/')
os.system('cp ./dep/enet/libenet.a ./dep/complib/')


# Output the build command
if platform.system() == 'Windows':
    print("Setting up for Windows")
    buildstring = 'g++ -o ./build/build.exe ./src/main.cpp -I./dep/imgui -I./dep/rlImGui -I./dep/enet/include -I./dep/raylib/src -L./dep/complib -lraylib -lrlImGui -lenet -lgdi32 -lwinmm'
    buildstring = buildstring + flags
    print(buildstring)

    with open('build.bat', 'w') as file:
        file.write(buildstring)


# Check for Linux
elif platform.system() == 'Linux':
    print("Setting up for Linux")
    buildstring = 'g++ -o ./build/build ./src/main.cpp -I./dep/imgui -I./dep/rlImGui -I./dep/enet/include -I./dep/raylib/src -L./dep/complib -lraylib -lrlImGui -lenet -lGL -lm -lpthread -ldl -lrt -lX11'
    buildstring = buildstring + flags
    print(buildstring)

    with open('build.sh', 'w') as file:
        file.write(buildstring)

    os.system('chmod +x build.sh')

# Check for macOS
elif platform.system() == 'Darwin':
    print("Setting up for macOS")
    buildstring = 'g++ -o ./build/build ./src/main.cpp -I./dep/imgui -I./dep/rlImGui -I./dep/enet/include -I./dep/raylib/src -L./dep/complib -lraylib -lrlImGui -lenet -framework OpenGL -framework Cocoa -framework IOKit -framework CoreVideo'
    buildstring = buildstring + flags
    print(buildstring)
    os.system('chmod +x build.sh')

    with open('build.sh', 'w') as file:
        file.write(buildstring)


