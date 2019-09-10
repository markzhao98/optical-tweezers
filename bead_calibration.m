% This program is supposed to calibrate the trap stiffness using the power
% spectrum density method, with opening a mat file.

% Load the mat file
load('0824_silica_0.72w_centered_8bit.mat')

% Begin calibration
otc_x = OTCalibMSD(Vx,S,dt,R,eta,T);
otc_y = OTCalibMSD(Vy,S,dt,R,eta,T);

otc_x = otc_x.calibrate( ...
    'verbose',true, ...
    'displayon',true ...
    );
otc_y = otc_y.calibrate( ...
    'verbose',true, ...
    'displayon',true ...
    );

otc_x.plottraj()
otc_y.plottraj()