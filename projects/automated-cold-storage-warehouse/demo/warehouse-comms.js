const store = [
  ["Supervisor", "STORE requested", "infeed"],
  ["PLC", "Interlocks satisfied", "infeed"],
  ["Radio link", "Command acknowledged by mobile controller", "transit"],
  ["Mobile controller", "Pallet deposited", "rack"],
  ["PLC", "Storage acknowledged", "rack"]
];
const retrieve = [
  ["Supervisor", "RETRIEVE requested", "rack"],
  ["PLC", "Interlocks satisfied", "rack"],
  ["Radio link", "Command acknowledged by mobile controller", "transit"],
  ["Mobile controller", "Pallet delivered", "infeed"],
  ["PLC", "Retrieval acknowledged", "infeed"]
];

export function stepsFor(command) {
  return command === "store" ? store : retrieve;
}
