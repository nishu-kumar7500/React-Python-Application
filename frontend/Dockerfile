# ---------- 1️⃣ Build stage ----------
FROM Node:20-alpine AS build

WORKDIR /app
# Install dependencies
COPY package.json ./
COPY vite.config.ts tsconfig.json ./

RUN npm install

# Copy source code and build
COPY . .
RUN npm run build

# ---------- 2️⃣ Production stage ----------
FROM nginx:alpine AS production

# Copy built files to Nginx html folder
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80 and start Nginx
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
