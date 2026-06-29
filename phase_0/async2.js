async function main() {
//await means: "pause right here until this ticket stops being pending — then give me the fulfilled value."
  try {
    const res = await fetch("https://api.github.com/users/omarscoppola1231231");

    if (!res.ok) {
      throw new Error(`Request failed with status ${res.status}`);
    }

    const data = await res.json();
    console.log(data.name, "-", data.public_repos, "public repos");
  } catch (error) {
    console.log("Something went wrong:", error.message);
  }
}

main();
