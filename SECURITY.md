# Security Policy

## Supported Versions

We actively support the following versions of the Supra Blockchain Metrics Exporter:

| Version  | Supported          |
| -------- | ------------------ |
| Latest   | :white_check_mark: |
| < Latest | :x:                |

We recommend always using the latest version to ensure you have the most recent security updates.

## Reporting a Vulnerability

We take security seriously and appreciate your efforts to responsibly disclose your findings.

### How to Report

**🚨 DO NOT open a public GitHub issue for security vulnerabilities.**

Instead, please report security vulnerabilities through one of these channels:

1. **Email**: Send details to security@blocksize.info
2. **GitHub Security Advisories**: Use the [Security tab](https://github.com/blocksize-capital-gmbh/supra-blockchain-metrics-exporter/security/advisories) in this repository
3. **Contact Form**: [Blocksize Security Contact](https://blocksize.info/contact/) (mark as security-related)

### What to Include

When reporting a vulnerability, please include:

- **Description**: A clear description of the vulnerability
- **Impact**: What could an attacker accomplish?
- **Reproduction**: Step-by-step instructions to reproduce the issue
- **Affected Versions**: Which versions are affected?
- **Environment**: Operating system, Docker version, deployment method
- **Proof of Concept**: If applicable, include a minimal example
- **Suggested Fix**: If you have ideas for fixing the issue

### Response Timeline

We commit to the following response times:

- **Initial Response**: Within 48 hours
- **Vulnerability Assessment**: Within 7 days
- **Fix Development**: Based on severity (Critical: 7 days, High: 14 days, Medium: 30 days)
- **Public Disclosure**: Coordinated with reporter after fix is available

### Severity Classification

We use the following severity levels:

#### Critical

- Remote code execution
- Privilege escalation to admin/root
- Complete authentication bypass
- Data exfiltration of sensitive information

#### High

- Authentication bypass for specific functions
- Unauthorized access to monitoring data
- Container escape vulnerabilities
- Denial of service affecting entire system

#### Medium

- Information disclosure (non-sensitive)
- Limited privilege escalation
- Cross-site scripting (if web interface exists)
- Dependency vulnerabilities with moderate impact

#### Low

- Local information disclosure
- Minor configuration issues
- Dependency vulnerabilities with minimal impact

## Security Best Practices

### For Users

1. **Keep Updated**: Always use the latest version
2. **Secure Configuration**: Follow security guidelines in README
3. **Access Control**: Limit access to metrics endpoints
4. **Network Security**: Use proper firewall rules
5. **Log Monitoring**: Monitor application logs for suspicious activity
6. **Container Security**: Use trusted base images and scan for vulnerabilities

### For Contributors

1. **Input Validation**: Validate all external inputs
2. **Authentication**: Implement proper authentication where needed
3. **Secrets Management**: Never commit secrets to version control
4. **Dependencies**: Keep dependencies updated and scan for vulnerabilities
5. **Code Review**: All security-related changes require thorough review
6. **Testing**: Include security testing in your contributions

## Security Features

Our exporter includes several security features:

- **Read-only Access**: Only reads log files, never writes
- **No Sensitive Data**: Metrics don't expose sensitive information
- **Container Security**: Runs as non-root user in containers
- **Dependency Scanning**: Automated vulnerability scanning with Trivy
- **Secret Scanning**: GitHub secret scanning enabled
- **Input Validation**: All external inputs are validated

## Known Security Considerations

### Log File Access

- The exporter requires read access to Supra node log files
- Ensure log files don't contain sensitive information
- Use proper file permissions to limit access

### Network Exposure

- Metrics endpoint exposes system information
- Implement proper access controls in production
- Consider using authentication proxy if needed

### Container Deployment

- Mount log files as read-only when possible
- Use security contexts to run as non-root
- Implement resource limits to prevent DoS

## Third-Party Dependencies

We maintain security through:

- **Automated Scanning**: Dependabot alerts for known vulnerabilities
- **Regular Updates**: Dependencies updated on a regular schedule
- **Minimal Dependencies**: Only essential dependencies included
- **Trusted Sources**: Dependencies from verified publishers when possible

## Incident Response

In case of a security incident:

1. **Immediate Response**: Security team notified within 1 hour
2. **Assessment**: Impact analysis completed within 24 hours
3. **Mitigation**: Temporary mitigations deployed if possible
4. **Communication**: Affected users notified through appropriate channels
5. **Post-Incident**: Review and improvements implemented

## Contact Information

- **Security Team**: security@blocksize.info
- **General Contact**: [Blocksize Contact Page](https://blocksize.info/contact/)
- **GitHub Security**: Use Security tab in this repository

## Acknowledgments

We appreciate security researchers and community members who help keep our project secure. Reporters of valid security vulnerabilities will be:

- Credited in our security advisories (with permission)
- Mentioned in release notes for fixes
- Invited to provide feedback on our security practices

---

**Remember**: When in doubt about a security issue, err on the side of caution and report it privately rather than publicly discussing it.
