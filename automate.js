const { exec } = require("child_process");

// Default variables
const _remote = "origin";

const run = (arg) => {
  return exec(`git ${arg}`, (error, stdout, stderr) => {
    if (error) {
      console.log(`error: ${error.message}`);
      return;
    }
    if (stderr) {
      console.log(`stderr: ${stderr}`);
      return;
    }
    //console.log(`stdout: ${stdout}`);
  });
};

const gitRemoteInfo = () => {
  return new Promise((resolve, reject) => {
    const cmd = run("remote -v");
    cmd.stdout.on("data", (output) => {
      const parse = output.split(" ");
      const match = /com[:\/](.+).git$/g.exec(parse[0]);
      const [userName, repoName] = match[1].split("/");
      resolve({ userName, repoName });
    });
  });
};

gitRemoteInfo().then((res) => {
  console.log(res.userName);
});
