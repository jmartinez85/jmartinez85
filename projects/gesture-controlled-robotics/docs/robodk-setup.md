# Gripper gesture simulation

The sample contains normalized thumb and index fingertip positions. The classifier uses separate opening and closing thresholds to prevent rapid toggling near a single threshold. A RoboDK integration can consume the state transitions as simulation inputs. The replay itself prints the gripper states and requires neither a camera nor a robot connection.
