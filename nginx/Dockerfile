FROM node:19-alpine3.17 as builder

WORKDIR /

COPY ./frontend /frontend

FROM nginx:alpine

COPY ./nginx /etc/nginx
COPY --from=builder /frontend /frontend

EXPOSE 80 80
EXPOSE 443 443

CMD ["nginx", "-g", "daemon off;"]