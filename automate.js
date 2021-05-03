const { exec } = require("child_process");
const readline = require("readline");

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
      const branch = parse[indx + 1];
      resolve(branch.trim());
    });
  });
};

const getAllLocalBranchName = () => {
  return new Promise((resolve, reject) => {
    const cmd = run("branch");
    cmd.stdout.on("data", (output) => {
      const parse = output.split(" ");
      const branches = [];
      for (item of parse) {
        if (item === "*" || item === "") {
          continue;
        }
        branches.push(item.trim());
      }
      resolve(branches);
    });
  });
};

const getAllRemoteBranchName = (remote) => {
  return new Promise((resolve, reject) => {
    const cmd = run("branch -r");
    cmd.stdout.on("data", (output) => {
      const parse = output.split(" ");
      let remoteBranches = [];
      for (item of parse) {
        if (item.includes(`${remote}/`) && !item.includes("HEAD")) {
          remoteBranches.push(item.split("/")[1].trim());
        }
      }
      resolve(remoteBranches);
    });
  });
};

const add = () => {
  run("add -A");
};

const commit = (message) => {
  if (!message) {
    const read = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });

    read.question("Type in your commit message: ", (answer) => {
      run(`commit -am "${answer}"`);
      read.close();
    });
  }
};

const branch = (name) => {
  if (!name) {
    const read = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });

    read.question(
      "Type in the name of the branch you want to make: ",
      (answer) => {
        run(`checkout -b ${answer}`);
        read.close();
      }
    );
  }
};

const fetch = (remote) => {
  run(`fetch ${remote}`);
};

const pull = (remote, b_name=null) => {
  if(!b_name) {
    getActiveBranchName().then(branchName=>{
    run(`pull ${remote} ${branchName}`);
  })}else{
    run(`pull ${remote} ${b_name}`);
  }
  
}

const push = (remote, b_name=null) => {
  if(!b_name) {
    getActiveBranchName().then(branchName=>{
    run(`push -u ${remote} ${branchName}`);
  })}else{
    run(`push -u ${remote} ${b_name}`);
  }
  
}




push("origin");
