import numpy as np

study_hours = np.array([2, 4, 3, 5])
practice_sessions = np.array([1, 2, 2, 3])

# New engineered feature = study_hours + practice_sessions
total_effort = study_hours + practice_sessions
print("Total Effort:", total_effort)
