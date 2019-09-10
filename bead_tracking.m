% This program is supposed to track the positions of the bead using the
% feature point detection technique, and save it to a mat file.

% Initialization
clear all; 
close all; 
clc;
edit('bead_tracking')

% User-defined variables for DVM
framerate = 10.8/10000; % Number of frames per second
radius = 12; % Partical radius in [pixel]
maxdistance = 4; % Maximum distance between objects in consecutive frames (default = 5 pixels)
maxhiatus = 1; % Maximum number of frames that can be skipped (default = 1 frame)
imin = 55; % Global intensity minimum (watch out for bit number!!)
imax = 255*3; % Global intensity maximum (watch out for bit number!!)

% User-defined variables for calibration
T = 293; % Temperature in [Kelvin]
eta = 8.9e-4; % Medium viscosity in [kg/(s m)]
R = 1e-6; % Bead radius in [m]
S = 6.5e-8; % Conversion factor in [m/pixel]
dt = 10.8/10000; % Sample time in [s]

% Load video file (in tiff stack format)
video = VideoFileTif(framerate);

dvm = DVM2DGauss(video);

% Tracking
framenumber = dvm.framenumber();
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
% save('.mat');