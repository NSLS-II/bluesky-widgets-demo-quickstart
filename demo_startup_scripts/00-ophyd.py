# flake8: noqa

from ophyd.sim import hw

# Import ALL simulated Ophyd objects in global namespace (borrowed from ophyd.sim)
globals().update(hw().__dict__)
del hw

# This should be changes in ophyd but we change it here for now.
# It tells the automatic plotting code that this is "of interest" for plotting.
det.kind = "hinted"
