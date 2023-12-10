% Processing the C output
output_variable = fileread('c_output.txt');
output_array1 = uint8(str2num(output_variable));
resized_matrix1 = reshape(output_array1, 100, 100);
fig1 = figure();  % Create a new figure
imshow(resized_matrix1);  % Display the image
title('C image');  % Set the title
drawnow;  % Force MATLAB to draw the figure

% Processing the Haskell output
output_variable2 = fileread('h_output.txt');
output_array2 = uint8(str2num(output_variable2));
resized_matrix2 = reshape(output_array2, 100, 100);
fig2 = figure();  % Create a new figure
imshow(resized_matrix2);  % Display the image
title('Haskell image');  % Set the title
drawnow;  % Force MATLAB to draw the figure

% Processing the Prolog output
output_variable3 = fileread('p_output.txt');
output_array3 = uint8(str2num(output_variable3));
resized_matrix3 = reshape(output_array3, 100, 100);
fig3 = figure();  % Create a new figure
imshow(resized_matrix3);  % Display the image
title('Prolog image');  % Set the title
drawnow;  % Force MATLAB to draw the figure
