FROM node:lts as build
WORKDIR /app
COPY web-ui/ /app
RUN npm ci
RUN npm run build

FROM alpine
RUN apk add --no-cache nginx py3-pip
RUN pip install honcho

COPY --from=build /app/build /usr/share/nginx/html
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/conf.d/watch-party.conf /etc/nginx/conf.d/watch-party.conf

RUN addgroup -S watch-party && adduser -S watch-party -G watch-party

RUN mkdir -p /var/lib/nginx/logs /var/log/nginx
RUN chown -R watch-party:watch-party /var/lib/nginx/
RUN chown -R watch-party:watch-party /var/log/nginx/

WORKDIR /app
USER watch-party:watch-party
ENV PATH="${PATH}:${HOME}/.local/bin"

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY Procfile .
COPY main.py .
ADD ./watch_party watch_party



CMD honcho start

