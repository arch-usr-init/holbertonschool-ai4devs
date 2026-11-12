// Select users whose score meets the passing threshold.
function getPassingUsers(users, minimumScore) {
  const passing = [];
  for (const user of users) {
    if (user.profile.score >= minimumScore) {
      passing.push(user.name);
    }
  }
  return passing;
}

const users = [
  { name: "Ada", score: 84 },
  { name: "Lin", score: 72 },
  { name: "Sam", score: 48 },
];
console.log("Passing users:", getPassingUsers(users, 70));
