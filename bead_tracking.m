% This program is supposed to track the positions of the bead using the
% feature point detection technique, and save it to a mat file.

% Initialization
clear all; 
close all; 
clc;
edit('bead_tracking')

% User-defined variables for DVM
framerate = 100/3; % Number of frames per second
radius = 4; % Partical radius in [pixel]
maxdistance = 2; % Maximum distance between objects in consecutive frames (default = 5 pixels)
maxhiatus = 1; % Maximum number of frames that can be skipped (default = 1 frame)
imin = 50; % Global intensity minimum (watch out for bit number!!)
imax = 250; % Global intensity maximum (watch out for bit number!!)

% User-defined variables for calibration
T = 297; % Temperature in [Kelvin]
eta = 8.9e-4; % Medium viscosity in [kg/(s m)]
R = 0.5e-6; % Bead radius in [m]
S = 258e-9; % Conversion factor in [m/pixel]
dt = 1/framerate; % Sample time in [s]

% Load video file (in tiff stack format)
video = VideoFileTif(framerate);

% Create DVM
dvm = DVM2DGauss(video);

% Video properties
filetype = dvm.filetype();
framenumber = dvm.framenumber();

% Read video
images = dvm.read(1,framenumber);

% Play video
dvm.play()

% Tracking
dvm = dvm.tracking('verbose', true, ...
    'displayon', true, ...
    'FramesToTrack', framenumber, ...
    'VideoPortion', 1, ...
    'Imin', imin, ...
    'Imax', imax, ...
    'Radius', radius);

% Tracing
dvm = dvm.tracing('verbose', true, ...
    'displayon', true, ...
    'MaxDistance', maxdistance, ...
    'MaxHiatus', maxhiatus);

% x-trajectory
Vx = dvm.Trajectories.X';
Vx = Vx - repmat(mean(Vx),size(Vx,1),1);

% y-trajectory
Vy = dvm.Trajectories.Y';
Vy = Vy - repmat(mean(Vy),size(Vy,1),1);

% Save to mat file
% save('.mat')
