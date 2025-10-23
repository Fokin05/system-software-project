Write-Host "=== System Software CI Process ===" -ForegroundColor Cyan

# Очистка
docker stop test-app 2>$null
docker rm test-app 2>$null

Write-Host "1. Building Docker image..." -ForegroundColor Yellow
docker build -t system-software-app:latest .

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Docker build failed!" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Docker image built successfully!" -ForegroundColor Green

Write-Host "2. Testing application..." -ForegroundColor Yellow
docker run -d --name test-app -p 8080:8080 system-software-app:latest
Start-Sleep -Seconds 5

Write-Host "3. Health check..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8080/health" -UseBasicParsing
    Write-Host "✅ Health: $($response.Content)" -ForegroundColor Green
} catch {
    Write-Host "❌ Health check failed" -ForegroundColor Red
}

Write-Host "4. Testing main endpoint..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8080" -UseBasicParsing
    Write-Host "✅ Main endpoint: ToDo List is working" -ForegroundColor Green
} catch {
    Write-Host "❌ Main endpoint failed" -ForegroundColor Red
}

Write-Host "5. Cleaning up..." -ForegroundColor Yellow
docker stop test-app
docker rm test-app

Write-Host "=== COMPLETED ===" -ForegroundColor Green
docker images | findstr "system-software-app"
