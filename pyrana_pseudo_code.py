# This file is to prototype the 
# layout of an object-oriented PIV
# code written in Python.
# The paradigm should be 
# similar to Prana, because
# the prana paradigm is pretty good
# (Job Lists, Jobs, Passes).
# 
# Some proposed exceptions:
# "Pairs" specify all
# the processing to be done to a 
# single pair of images.
# They contain lists of "passes",
# and passes are defined by a number
# of user-defined criteria that
# are not updated iteratively,
# like initial grid spacing,
# interrogation region size, 
# etc. Although within this
# paradigm, any of these paramters
# may be iteratively updated.
# The defining feature of passes
# is that the number of passes
# is determined by the user,
# and does not grow iteratively.
#
# "Passes" contain lists of
# iterations, and iterations
# proceed until convergence
# or a max number of iterations
# is reached. The number of 
# iterations is not specified
# a-priori (except in the sense
# that a maximum number of iterations
# may be specified). For non-iterative
# passes, the max number
# of passes is just set to 1.
#
# "Correlations" are single pairs
# of interrogation regions (IRs) 
# that are used to calculate a single
# vector. The Correlation object
# does not need to know from whence
# the regions came; IRs are 
# extracted from images during 
# each "iteration."
# The correlation object
# should contain attributes including
# the IRs themselves, the windowing
# array, the resultant correlation plane,
# and the calculated vector.
# The Correlation object should
# also have separate methods for 
# SCC, RPC, FMC, APC, etc.
# and a corresponding attribute
# for "correlation type" (or something)
# that specifies which one to use.
# This would sensibly be inherited
# from the "Pass" object.


JobList (list of jobs)
    Job (list of snapshots)
       Snapshot (list of cameras)
            Camera (list of pairs)
                 Pair 
                    Pass
                       Iteration
                           Correlation;

# The structures might be organized like this
# This looks like a lot to pass around, but
# we won't have to actually pass all this around
# because methods are concise.
JobList[L].SnapShot[S].Camera[C].Pair[k].Pass[n].Iteration[i];

# Count the number of jobs
NumJobs = len(JobList);

# Execute all the jobs.
for J = 1 : NumJobs:
   JobList[L].Execute();
   
# Number of snapshots:
for S = 1 : len(SnapShot):
    SnapShot[S].Execute();

# etc etc. The complicated stuff only
# begins at the "Pass" level.

# I think the call will be something like
# Pass.Method = "Deform";
# Pass.Execute();

# Below is some pseudo-code
# for how I envision a single
# iterative Pass being procesed.

# Initialize the "stop iterations" flag
stop_iterations = False;

# Loop over processing until 
# an escape condition is reached.
# stop_iterations will return true
# if the max number of iterations is 
# reached, or if the pass converges.
# For non-iterative passes,
# Pass.MaxIterations = 1
while stop_iterations is False:
    
    # Add an iteration to the pass.
    # Inside of here will be
    # Pass.NumIterations += 1;
    Pass.Iterations.Append();
    
    # Read the current number of Iterations
    # and compare to the maximum specified
    # number of iterations
    if Pass.NumIterations >= Pass.MaxIterations:
        # This will cause the loop to end
        # after the next iteration. But it 
        # won't escape the current iteration.
        stop_iterations = True;
        
    # Grid the image
    # This updates Pass.Iteration[n].X and Pass.Iteration[n]Y
    # which could start out as None
    # Grid needs to be a method of a
    # Pass object because it needs 
    # access to at least two iterations
    # This also handles Discrete Window Offset.
    Pass.Grid();
    
    # Do deformation if requested
    # This updates Pair.Images
    # based on the most recent
    # pass values of:
    # Pass.X, Pass.Y, Pass.Iteration[n].U, Pass.Iteration[n].V;  
    # 
    # Pass should have attributes (Images)
    if do_deform:
        Pass.DeformImages();
        
    # This does the correlation
    # Remember, Pass has access
    # to the images.
    # This should correlate
    # using the last iteration
    # in the list of iterations.
    Pass.Correlate()
    
    # This does validation, smoothing, POD, 
    # whatever, between (or after) iterations.
    # The [-1] means "last element in list"
    Pass.PostProcess()
        
    # Check convergence
    # Compares the last two 
    # iterations, e.g., 
    # Pass.Iteration[n].U,V and Pass.Iteration[n - 1].U,V
    # This will set Pass.HasConverged = True or False
    stop_iterations = Pass.CheckConvergence();





