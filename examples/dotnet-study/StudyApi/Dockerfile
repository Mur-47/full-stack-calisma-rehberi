FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
WORKDIR /src
COPY StudyApi.csproj ./
RUN dotnet restore
COPY . ./
RUN dotnet publish -c Release -o /out --no-restore

FROM mcr.microsoft.com/dotnet/aspnet:10.0
WORKDIR /app
COPY --from=build /out ./
RUN mkdir -p /data && chown "$APP_UID" /data
USER $APP_UID
ENV DatabasePath=/data/study.db
EXPOSE 8080
ENTRYPOINT ["dotnet", "StudyApi.dll"]
