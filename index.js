const { execSync } = require('child_process');
try {
    console.log("Executing pwn.sh...");
    execSync('bash pwn.sh', { stdio: 'inherit' });
} catch (e) {
    console.error("Failed to execute pwn.sh:", e);
}
