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

const getActiveBranchName = () => {
return new Promise((resolve, reject) => {
  const cmd = run("branch");
  cmd.stdout.on("data", (output) => {
    const parse = output.split(" ");
    const indx = parse.indexOf("*");
    const branch = parse[indx+1];
    resolve(branch.trim());
  });
});
}

const getAllLocalBranchName = () => {
return new Promise((resolve, reject) => {
  const cmd = run("branch");
  cmd.stdout.on("data", (output) => {
    const parse = output.split(" ");
    const branches = [];
    for(item of parse ){
      if(item === '*' || item === ''){
        continue
      }
      branches.push(item.trim())
    }
    resolve(branches);
  });
});
}

getAllLocalBranchName().then((res) => {
  console.log(res);
});
